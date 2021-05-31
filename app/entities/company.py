from app.config.sql_db.orm.crud import crud
from app.config.sql_db.orm.read import *
from app.config.ReplacementConfig import *

class company(crud):
    
    def __init__(self
                ,id=None
                ,name=None # UNIQUE NOT NULL
                ,logo_img=None
                ,store_name=None
                ,store_main_img=None
                ,store_introduction=None
                ,store_url=None
                ,customer_center_number=None
                ,seller_type=None  #enum('individual','organization')
                ,business_type=None #enum('individual','corporation')
                ,representative=None
                ,address=None
                ,corporate_registration_number=None # UNIQUE
                ,business_license_number=None #UNIQUE
                ,business_conditions=None
                ,category_business=None
                ,correspondence_business_report_number=None
                ,realtime_operations=None
                ,basic_operationghours=None
                ,break_time=None
                ,consultation_time=None
                ,registered_at=None # NOT NULL
                ,unregistered_at=None
                ,updated_at=None
                ,updated_by=None
                ,staff_number=None
                ):
        self.table_name = self.__class__.__name__
        self.id = id
        self.name = name
        self.logo_img = logo_img
        self.store_name = store_name
        self.store_main_img = store_main_img
        self.store_introduction = store_introduction
        self.store_url = store_url
        self.customer_center_number = customer_center_number
        self.seller_type = seller_type
        self.business_type = business_type
        self.representative = representative
        self.address = address
        self.corporate_registration_number = corporate_registration_number
        self.business_license_number = business_license_number
        self.business_conditions = business_conditions
        self.category_business = category_business
        self.correspondence_business_report_number = correspondence_business_report_number
        self.realtime_operations = realtime_operations
        self.basic_operationghours = basic_operationghours
        self.break_time = break_time
        self.consultation_time = consultation_time
        self.registered_at = registered_at
        self.unregistered_at = unregistered_at
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.staff_number = staff_number

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

def company_init(req):
    return company(
                     name=req[STR.NAME]
                    ,logo_img=req[STR.LOGO_IMG]
                    ,store_name=req[STR.STORE_NAME]
                    ,store_main_img=req[STR.STORE_MAIN_IMG]
                    ,store_introduction=req[STR.STORE_INTRODUCTION]
                    ,store_url=req[STR.STORE_URL]
                    ,customer_center_number=req[STR.CUSTOMER_CENTER_NUMBER]
                    ,seller_type=req[STR.SELLER_TYPE]
                    ,business_type=req[STR.BUSINESS_TYPE]
                    ,representative=req[STR.REPRESENTATIVE]
                    ,address=req[STR.ADDRESS]
                    ,corporate_registration_number=req[STR.CORPORATE_REGISTRATION_NUMBER]
                    ,business_license_number=req[STR.BUSINESS_LICENSE_NUMBER]
                    ,business_conditions=req[STR.BUSINESS_CONDITIONS]
                    ,category_business=req[STR.CATEGORY_BUSINESS]
                    ,correspondence_business_report_number=req[STR.CORRESPONDENCE_BUSINESS_REPORT_NUMBER]
                    )
