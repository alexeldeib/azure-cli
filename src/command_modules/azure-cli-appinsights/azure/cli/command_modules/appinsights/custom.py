def query(cmd, app_id):
    from texttable import Texttable
    from ._client_factory import appinsights_data_plane_client
    client = appinsights_data_plane_client(app_id)
    t = Texttable()
    t.add_rows(client.get_query('availabilityResults | take 10 | project name, location, duration').tables[0].rows)
    print(t.draw())