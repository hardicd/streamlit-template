import datetime
import ee
import streamlit as st
import geemap.foliumap as geemap
st.set_page_config(layout="wide")



def app():
    st.title("Change Detection")
    json_private_key = {
  "type": "service_account",
  "project_id": "change-370819",
  "private_key_id": "cdd38e86bb6112d0503fe20d7d69852e5a5e6be3",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDhO1LO8BEsdwxX\nEJC0UmRHW3EUKwzJRSjUwNr6QOr8B0LG25jY2Qpw8WJK19+wxCy/sIWqWJa1AkqF\nVniRqNMnTBpznHnQ0bBzDgJkDqrRkhsBs+mTjy/ikp5scHP6N4rqKUCngvfcxzIs\nNs9TYjqS1pM8Qjmt025g7zy000YcglyscXcdK8/jO6L6AUjZGYe48vGOM18+/6XD\nSqTw3Orb0jYSaHfoeNayGPdJgUDK8Y4Kc/hgYrCDxTNKogFfg3qTT4TZW7QcoxrK\nk6G5HIbdbQNus5fRqxiZmzlfDvkohLso+jtQIinQtiYqz1bMkydr9bcNKoPfn6aW\n+ibHqKXhAgMBAAECggEABdGlCuChPkoDFnAV9Pqt9DlUu2XTVOiFrLLLgCyo2thg\ngse4nrLuIKCJNBAjYNXoprkrnYzgCTl6bbsgA/oIc9r0/KiobbCFLlZzJweepSnG\nVdhtP+6H7lgbDLJ+ZJKxHZScQtemNLIsGyqoAj+m7hU/b46cc9+4WdEZ0JLRcboQ\nvLW/Ga0Ajv0ZX6lMIFvvMcDSXCI7FFPYHYVabI4ZzxBv+Jyt6/BenAWv0nkvDJuu\n8hY6jSW5wU9uJLalyoUvSkpsXfJv6bDnoMh2Fbqj8ZEech7ijGBIcpuG6kSMniAE\nMqBEzFSTOLodxXseyzuWHrsaE/0LMfZHBOYxrwKJcwKBgQDypKcwMB48TIutKJuE\n3k5fET0+faR4avFcgyZOjOyUZ3+l1ORNp0J+lPw1lmHvxsKJzbEm6EH/yjmzXLBS\nl5Tif+D2+ybH4REQ01yW7xGack1yODyCtt/pS5aXvo9Cw+WeoXAVDI/8BA74GusU\n55M7Sv4vyJggV48x27GNfykdkwKBgQDtoU6TuFiCVBY9a5dwuP0r4KHziAO3/8nH\nHczNpcF2W2NqnDfBbs3iufVkw/rTDRggnw/7nwtCrIOYGV5xPnkrKwla4lgFfP2E\nJ27aeoE1UGCa0++pL9Xe6QXjTV8lpZ2TbG4jp0daryTZZx91oDLMAIbqkJRtaKUV\noLdps4L3OwKBgQCBuG89fuwbNp0R9Py32xWxE4lXiFpOmnXxDJiFNCgi6vY+VQO9\nVCdjfwkbKQuw4eUNQS9taowmURnp/yqw7SMGuHEv+XNxNq0l/qmoc6VImcU3xELt\naxFoKyYWeCUk/5AZ75r5Vd8AT7clA1cctPVspJoiN67E06rVb+uLhykXCwKBgQCR\nKo26KE/Jrly3wNaPAjOHbn8BKwI6kYROo6HNr4j0KPge1Lgq7unPrBKBMEg2TjWD\nGCjHam2SmZj6feT4AVY8TNo2LzfegnDNHtnVlikAzM13SCmMjbB1sJzsMwQBF5+f\nxAm0tigc+gnk1d6eGPNvNJM3EIPcIqVXBQuHAybqqQKBgQDaXnEgdhb/iz6gwHTV\njc6FKtR+A+i5G9JKfc4JRHPpkYsbKNYv+W0Gp6oeLIumTqTkIXK1Uhjv5+qWoE1i\nLW4hhzLwBV6HvrXD+ef5exehK88Hl+pkvVpOm5TEqmPtaAsXqtfQ8yfFD2YvmJg2\no2m6keG1mXre7Wd189iXr4FIBA==\n-----END PRIVATE KEY-----\n",
  "client_email": "eogmap@change-370819.iam.gserviceaccount.com",
  "client_id": "116630732010339894634",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/eogmap%40change-370819.iam.gserviceaccount.com"
}
    service_account = 'eogmap@change-370819.iam.gserviceaccount.com'
    credentials = ee.ServiceAccountCredentials(service_account, json_private_key)
    ee.Initialize(credentials)
    col1, col2 = st.columns([4, 1])
    Map = geemap.Map()
    Map.add_basemap("HYBRID")

    markdown = """
        - [Dynamic World Land Cover](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_DYNAMICWORLD_V1?hl=en)
        - [ESA Global Land Cover](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCover_v100)
    
    """

    with col2:
        # set the basemap default map center and zoom level
        longitude = st.number_input("Longitude", -180.0, 180.0, -95.358421)
        latitude = st.number_input("Latitude", -90.0, 90.0, 29.749907)
        zoom = st.number_input("Zoom", 0, 20, 11)
        Map.setCenter(longitude, latitude, zoom)

        # add the fields to the sidebar where you enter the date ranges
        start = st.date_input("Start Date for before image(2015/07/01, archive limit)", datetime.date(2020, 1, 1))
        end = st.date_input("End Date for before image", datetime.date(2021, 1, 1))
        start2 = st.date_input("Start Date for after image", datetime.date(2020, 1, 1))
        end2 = st.date_input("End Date for after image", datetime.date(2021, 1, 1))

        # convert the dates into a usable format
        start_date = start.strftime("%Y-%m-%d")
        end_date = end.strftime("%Y-%m-%d")
        start_date2 = start2.strftime("%Y-%m-%d")
        end_date2 = end2.strftime("%Y-%m-%d")

        # select image collection fpr the first sentinel 2 image
        s2_before = ee.ImageCollection("COPERNICUS/S2_HARMONIZED") \
            .filterDate(start_date, end_date) \
            .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 2))
        # reduce to single image
        s2_before_red = s2_before.reduce(ee.Reducer.median())

        # select image collection fpr the second sentinel 2 image
        s2_after = ee.ImageCollection("COPERNICUS/S2_HARMONIZED") \
            .filterDate(start_date2, end_date2) \
            .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 2))
        # reduce to single image
        s2_after_red = s2_after.reduce(ee.Reducer.median())


        #set the visibillity parameters for the first image
        s2_before_vis = {'bands': ['B4_median', 'B3_median', 'B2_median'], 'min': 0, 'max': 3000}
        # visuialization parameters for the lclu change results
        VisParams = {'palette': ['#FFFFFF', '#FF0000'], 'min': 0, 'max': 1}
        VisParams2 = {'palette': ['#FFFFFF', '#FF0000'], 'min': 0, 'max': 1}

        #pull in the Dynamic Earth model
        region = ee.Geometry.BBox(-179, -89, 179, 89)
        dw = geemap.dynamic_world(region, start_date, end_date, return_type="hillshade")
        dw2 = geemap.dynamic_world(region, start_date2, end_date2, return_type="hillshade")

        # select the lclu model for the first date
        dw_before_coll = ee.ImageCollection('GOOGLE/DYNAMICWORLD/V1')\
            .filterDate(start_date, end_date)
        # select the lclu model for the first date
        dw_after_coll = ee.ImageCollection('GOOGLE/DYNAMICWORLD/V1') \
            .filterDate(start_date2, end_date2)

        # mosaic and clip lclu
        dw_before_mos = dw_before_coll.mosaic()
        dw_after_mos = dw_after_coll.mosaic()
        # select the lclu bands
        class_before = dw_before_mos.select('bare')
        class_after = dw_after_mos.select('bare')
        # select the lclu bands
        class_before2 = dw_before_mos.select('built')
        class_after2 = dw_after_mos.select('built')

        ##BARE
        bare_before = class_before
        bare_after = class_after
        new_bare = bare_before.lt(0.25).And(bare_after.gt(0.4))
        new_bare = new_bare.updateMask(new_bare)

        ##BUILT
        bare_before2 = class_before2
        bare_after2 = class_after2
        new_built = bare_before2.lt(0.25).And(bare_after2.gt(0.55))
        new_built = new_built.updateMask(new_built)

        #add the layers to the map
        layers = {
            "Landcover Classification before": geemap.ee_tile_layer(dw, {}, "Dynamic World Land Cover Before"),
            "Sentinel Imagery before": geemap.ee_tile_layer(s2_before_red, s2_before_vis, "S2 Before image"),
            "Sentinel Imagery after": geemap.ee_tile_layer(s2_after_red, s2_before_vis, "S2 after image"),
            "Landcover Classification after": geemap.ee_tile_layer(dw2, {}, "Dynamic World Land Cover After"),
            "New Bare Ground": geemap.ee_tile_layer(new_bare, VisParams, "New Bare"),
            "New Built-up area": geemap.ee_tile_layer(new_built, VisParams2, "New Bare"),

        }

        #Add layers that can be selected for the left and right maps
        options = list(layers.keys())
        left = st.selectbox("Select a left layer", options, index=1)
        right = st.selectbox("Select a right layer", options, index=0)
        left_layer = layers[left]
        right_layer = layers[right]
        Map.split_map(left_layer, right_layer)

        #add the legend to the map
        legend = st.selectbox("Select a legend", options, index=options.index(right))
        if legend == "Dynamic World":
            Map.add_legend(
                title="Dynamic World Land Cover",
                builtin_legend="Dynamic_World",
            )
        elif legend == "Dynamic World after":
            Map.add_legend(title="Dynamic World Land Cover", builtin_legend="Dynamic_World")

        #add that data links to the products used in the map
        with st.expander("Data sources"):
            st.markdown(markdown)


    with col1:
        Map.to_streamlit(height=750)