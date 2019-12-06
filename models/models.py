# -*- coding: utf-8 -*-

from odoo import models, fields, api


class darazCategory(models.Model):
    _inherit = "product.category"

    leaf=fields.Boolean("Leaf",default=False)
    categoryId=fields.Integer("Daraz Category ID")


    def getCategories(self):
        import requests
        import hashlib
        from datetime import datetime
        import pytz

        url = "https://api.sellercenter.daraz.pk"
        key="A8B6GG7x7O45ffCQJfkydp1eTHv9D8RfTOEc2lLkfZhpQBUWiMa3qg1K"
        signature=hashlib.sha256(key.encode('utf-8')).hexdigest()
        now = datetime.now()
        isoDate=now.isoformat()
        print(isoDate)
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        utc = "+5:00"
        datestr = str(year) + "-" + str(month) + "-" + str(day) + "T" + str(hour) + ":" + str(minute) + ":" + str(
            second) + utc
        action="GetCategoryTree"
        format="json"
        userId="zmmart@gmail.com"
         #querystring = {"Action": action, "Format": format, "Timestamp": datestr,
        #                "UserID": userId, "Version": "1.0",
        #                "Signature": signature}
        querystring = {"Action": "GetCategoryTree", "Format": "json", "Timestamp": "2019-12-03T12%3A36%3A37%2B00%3A00",
                       "UserID": "zmmart%40gmail.com", "Version": "1.0",
                       "Signature": "8d7219e63f7459038aaa2cec9b6258e43272fe284b6e54d5c5b02de648520f76"}
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Accept': "*/*",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

