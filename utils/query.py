select_distinct_export_dates_query = """
                                     select distinct export_date
                                     from {0}
                                     where export_date between DATE '{1}' and DATE '{2}'
                                     """
