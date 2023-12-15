from uuid import uuid4

from django.contrib.admin import TabularInline, ModelAdmin
from django.db.models import Count
from django.forms import BaseInlineFormSet
from django.urls import reverse
from django.utils.html import format_html
from django.utils.timezone import localtime

from django_ledger.admin.coa import ChartOfAccountsInLine
from django_ledger.models import EntityUnitModel
from django_ledger.models.entity import EntityModel, EntityManagementModel


class EntityManagementInLine(TabularInline):
    model = EntityManagementModel
    extra = 1
    fields = [
        'user'
    ]


class EntityUnitModelInLineFormSet(BaseInlineFormSet):

    def save_new(self, form, commit=True):
        setattr(form.instance, self.fk.name, self.instance)
        if commit:
            unit_model = EntityUnitModel.add_root(
                instance=super().save_new(form, commit=False)
            )
            return unit_model
        return super().save_new(form, commit=False)


class EntityUnitModelInLine(TabularInline):
    model = EntityUnitModel
    formset = EntityUnitModelInLineFormSet
    extra = 0
    readonly_fields = [
        'slug'
    ]
    fields = [
        'slug',
        'name',
        'document_prefix',
        'active',
        'hidden'
    ]


class EntityModelAdmin(ModelAdmin):
    list_display = [
        'name',
        'accrual_method',
        'last_closing_date',
        'hidden',
        'get_coa_count',
        'add_ledger_link',
        'balance_sheet_link',
        'income_statement_link',
        'cash_flow_statement_link'
    ]
    readonly_fields = [
        'depth',
        'path',
        'numchild',
        'last_closing_date',
        'default_coa'
    ]
    fieldsets = [
        (
            'Entity Information', {
                'fields': [
                    'name',
                    'admin',
                    'fy_start_month',
                    'accrual_method',
                    'hidden',
                    'picture'
                ]
            }
        ),
        (
            'Contact Information', {
                'fields': [
                    'address_1',
                    'address_2',
                    'city',
                    'state',
                    'zip_code',
                    'email',
                    'website',
                    'phone'
                ]
            }
        ),
        (
            'Chart of Accounts', {
                'fields': [
                    'default_coa'
                ]
            }
        )
    ]
    inlines = [
        ChartOfAccountsInLine,
        EntityUnitModelInLine,
        EntityManagementInLine
    ]
    actions = [
        'add_code_of_accounts'
    ]

    class Meta:
        model = EntityModel

    def get_queryset(self, request):
        qs = super().get_queryset(request=request)
        qs = qs.annotate(Count('chartofaccountmodel'))
        if request.user.is_superuser:
            return qs
        return qs.for_user(user_model=request.user)

    def add_ledger_link(self, obj):
        add_ledger_url = reverse('admin:django_ledger_ledgermodel_add')
        return format_html('<a class="addlink" href="{url}?entity_slug={slug}">Add Ledger</a>',
                           url=add_ledger_url,
                           slug=obj.slug)

    def balance_sheet_link(self, obj: EntityModel):
        add_ledger_url = reverse(
            viewname='django_ledger:entity-bs',
            kwargs={
                'entity_slug': obj.slug
            })
        return format_html('<a class="viewlink" href="{url}">View</a>',
                           url=add_ledger_url,
                           slug=obj.slug)

    balance_sheet_link.short_description = 'Balance Sheet'

    def income_statement_link(self, obj: EntityModel):
        add_ledger_url = reverse(
            viewname='django_ledger:entity-ic',
            kwargs={
                'entity_slug': obj.slug
            })
        return format_html('<a class="viewlink" href="{url}">View</a>',
                           url=add_ledger_url,
                           slug=obj.slug)

    income_statement_link.short_description = 'P&L'

    def cash_flow_statement_link(self, obj: EntityModel):
        add_ledger_url = reverse(
            viewname='django_ledger:entity-cf',
            kwargs={
                'entity_slug': obj.slug
            })
        return format_html('<a class="viewlink" href="{url}">View</a>',
                           url=add_ledger_url,
                           slug=obj.slug)

    cash_flow_statement_link.short_description = 'Cash Flow'

    def add_code_of_accounts(self, request, queryset):
        for entity_model in queryset:
            entity_model.create_chart_of_accounts(
                coa_name=f'{entity_model.name} CoA {localtime().isoformat()}',
                commit=True,
                assign_as_default=False
            )

    def get_coa_count(self, obj):
        return obj.chartofaccountmodel__count

    get_coa_count.short_description = 'CoA Count'

    def save_model(self, request, obj, form, change):
        if not change:
            if obj.uuid is None:
                obj.uuid = uuid4()
            EntityModel.add_root(instance=obj)
            return
        super().save_model(request, obj, form, change)
