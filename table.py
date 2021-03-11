import pandas as pd
import numpy as np
from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import TableColumn, DataTable


def table_tab(data):
    d = data.groupby('name')['arr_delay'].describe()
    d['mean'] = d['mean'].round(1)
    d['std'] = d['std'].round(1)

    c = ColumnDataSource(d)
    flights_table = DataTable(
        source=c,
        columns=[
            TableColumn(field='name', title='ایرلاین'),
            TableColumn(field='count', title='تعداد پرواز'),
            TableColumn(field='mean', title='میانگین تأخیر'),
            TableColumn(field='std', title='انحراف استاندارد تأخیر'),
            TableColumn(field='min', title='بیشینه‌ی تأخیر'),
            TableColumn(field='25%', title='۲۵٪'),
            TableColumn(field='50%', title='۵۰٪'),
            TableColumn(field='75%', title='۷۵٪'),
            TableColumn(field='max', title='بیشینه‌ی تأخیر'),
        ],
        width=1200
    )
    tab = Panel(child=flights_table, title='خلاصه‌ی تأخیرها')

    return tab
