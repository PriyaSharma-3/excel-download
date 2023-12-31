from django.shortcuts import render, redirect  
from django.http import HttpResponse
from .forms import ConsumerForm
from .models import Consumer
import csv

def index(request):
    if request.method == 'POST':
            form = ConsumerForm(request.POST) 

            Username = request.POST['Username']
            Date_Time = request.POST['Date_Time']

            try:
                consumer = Consumer.objects.get(Username_Consumer=Username,Date_Time_Consumer=Date_Time)   

                request.session['Username'] = Username
                request.session['Date_Time'] = Date_Time

            except Consumer.DoesNotExist:
                consumer = None
                         
            if consumer is not None:
                return redirect('/consumer_excel')                                           
            else:
                return render(request, 'index.html')

    return render(request,"index.html") 

def consumer_excel(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="consumer(MMC).csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
            'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
            'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
            'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
            'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
            'NoofDigits','SurveyorRemark'])

    Username=request.POST.get('Username_Consumer')
    Date_Time=request.POST.get('Date_Time_Consumer')

    if Username == 'all':

        for consumer in Consumer.objects.all().filter(Date_Time__contains=Date_Time).values_list('Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
            'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
            'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
            'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
            'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
            'NoofDigits','SurveyorRemark'):
            writer.writerow(consumer)
    else:

        for consumer in Consumer.objects.all().filter(Username=Username,Date_Time__contains=Date_Time).values_list('Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
            'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
            'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
            'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
            'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
            'NoofDigits','SurveyorRemark'):
            writer.writerow(consumer)

    return response

def index(request):
    if request.method == 'POST':
            form = ConsumerForm(request.POST) 

            Username = request.POST['Username']
            Date_Time = request.POST['Date_Time']

            try:
                consumer2 = Consumer.objects.get(Username_Consumer2=Username,Date_Time_Consumer2=Date_Time)   

                request.session['Username'] = Username
                request.session['Date_Time'] = Date_Time

            except Consumer.DoesNotExist:
                consumer2= None
                         
            if consumer2 is not None:
                return redirect('/consumer_excel2')                                           
            else:
                return render(request, 'index.html')

    return render(request,"index.html") 

def consumer_excel2(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="consumer(All).csv"'},
    )

    writer = csv.writer(response)

    writer.writerow(['UN_MIGR_ID','TP_COMM_TY','DEVICE_TYP','TP_DIS_CON','TP_FUNC','STATUS','MOUNTING','NETWORK_TY','OWNER_TYP','PHASE_CON','REMARKS','SUB_DIV_CO','SUB_DIV_NM',
        'TP_SUBTYE','TP_TYPE','TP_WARD_CD','TP_SC_NUM','TP_SL_NUM','BUILD_ID','POLE_ID','P_POLE_ID','DT_CODE','CONSUMER_N','CATEGORY','MT_MAKE','KWH','CIRCLE',
        'DIV','SECTION','NEW_SC_NUM','MOBILE_NO','FLAT_NO','ADDRESS','ADDRESS_1','AMR_INSTAL','CT_RATIO','MAXIMUM_DE','METER_AVAI','METER_BOX','METER_LOCA',
        'HEIGHT_5FT','NOMINAL_VO','SEAL_CONDI','SEAL_TYPE','BYPASS','THEFT','BILL_DELIV','BILL_SHOWN','NEI_CON_NO','NEI_MET_NO','DOOR_LOCK','METER_PHOT',
        'BILL_PHOTO','PSS_CODE','GSS_CODE','DATE_TIME','PSS_NAME','GSS_NAME','KW','ID','SURVEYID','LATITUDE','LONGITUDE','USERNAME','FEEDERNAME','OLDACCOUNT',
        'ADDRESS3','COMMUNICAT','DISPLAYCON','METERSTATU','TYPE','SUBTYPE','OTHERPHOTO','NOOFDIGITS','MeterMake'])

    Username=request.POST.get('Username_Consumer2')
    Date_Time=request.POST.get('Date_Time_Consumer2')

    if Username == 'all':

        for consumer2  in Consumer.objects.all().filter(Date_Time__contains=Date_Time).values_list('NewAccountNumber','PhaseConnection','SurveyorRemark','SubDivision','BuildingReferenceNumber','ConnectedPoleNo','DTCode','ConsumerName','Category',
            'kWh','Section','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','AMRInstalled','CTRatio','MaximumDemand','MeterAvailability',
            'MeterBox','MeterLocation','HeightGT5ft','NominalVoltage','SealCondition','SealType','Bypass','Theft','BillDelivered','BillShown',
            'NeighbouringConsumerNo','NeighbouringMeterNo','ConsumerDoorLock','MeterPhoto','BillPhoto','Date_Time','Id','SurveyId','Latitude',
            'Longitude','Username','FeederName','OldAccountNumber','Address3','CommunicationType','DisplayCondition','MeterStatus','Type',
            'SubType','OtherPhoto','NoofDigits','MeterMake'):
            consumer2= list(consumer2)   
            
            consumer2.insert(0,"") 
            consumer2.insert(1,"")
            consumer2.insert(2,"Consumer")
            consumer2.insert(4,"LV Consumer")
            consumer2.insert(5,"Exiisting")
            consumer2.insert(6,"Overhead")
            consumer2.insert(7,"LV")
            consumer2.insert(8,"Company Owned")
            consumer2.insert(11,"")
            consumer2.insert(13,"Unknown")
            consumer2.insert(14,"Unknown")
            consumer2.insert(15,"")
            consumer2.insert(16,"")
            consumer2.insert(17,"")
            consumer2.insert(20,"")
            consumer2.insert(24,"")
            consumer2.insert(26,"") 
            consumer2.insert(27,"") 
            consumer2.insert(53,"")
            consumer2.insert(54,"")
            consumer2.insert(56,"")
            consumer2.insert(57,"")
            consumer2.insert(58,"")

            consumer2_main = tuple(consumer2)
         

            writer.writerow(consumer2_main)
            
    return response

def logout(request):
    return render(request,"login.html")


# def index(request):
#     if request.method == 'POST':
#             form = ConsumerForm(request.POST) 

#             Username = request.POST['Username']
#             Date_Time = request.POST['Date_Time']

#             try:
#                 consumer1 = Consumer.objects.get(Username_Consumer1=Username,Date_Time_Consumer1=Date_Time)   

#                 request.session['Username'] = Username
#                 request.session['Date_Time'] = Date_Time

#             except Consumer.DoesNotExist:
#                 consumer1= None
                         
#             if consumer1 is not None:
#                 return redirect('/consumer_excel1')                                           
#             else:
#                 return render(request, 'index.html')

#     return render(request,"index.html") 

# def consumer_excel1(request):
#     response = HttpResponse(
#         content_type='text/csv',
#         headers={'Content-Disposition': 'attachment; filename="consumer(ITI).csv"'},
#     )

#     writer = csv.writer(response)
#     writer.writerow(['Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
#             'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
#             'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
#             'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
#             'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
#             'NoofDigits','SurveyorRemark'])

#     Username=request.POST.get('Username_Consumer1')
#     Date_Time=request.POST.get('Date_Time_Consumer1')

#     if Username == 'all':

#         for consumer1 in Consumer.objects.all().filter(Username__contains="iti",Date_Time__contains=Date_Time).values_list('Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
#             'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
#             'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
#             'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
#             'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
#             'NoofDigits','SurveyorRemark'):
#             writer.writerow(consumer1)
#     else:

#         for consumer1 in Consumer.objects.all().filter(Username=Username,Date_Time__contains=Date_Time).values_list('Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
#             'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
#             'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
#             'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
#             'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
#             'NoofDigits','SurveyorRemark'):
#             writer.writerow(consumer1)

#     return response




# def index(request):
#     if request.method == 'POST':
#             form = ConsumerForm(request.POST) 

#             Username = request.POST['Username']
#             Date_Time = request.POST['Date_Time']

#             try:
#                 TSA = Consumer.objects.get(Username_TSA=Username,Date_Time_TSA=Date_Time)   

#                 request.session['Username'] = Username
#                 request.session['Date_Time'] = Date_Time

#             except Consumer.DoesNotExist:
#                 TSA= None
                         
#             if TSA is not None:
#                 return redirect('/consumer_TSA')                                           
#             else:
#                 return render(request, 'index.html')

#     return render(request,"index.html") 

# def consumer_TSA(request):
#     response = HttpResponse(
#         content_type='text/csv',
#         headers={'Content-Disposition': 'attachment; filename="consumer(TSA).csv"'},
#     )

#     writer = csv.writer(response)
#     writer.writerow(['Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
#             'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
#             'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
#             'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
#             'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
#             'NoofDigits','SurveyorRemark'])

#     Username=request.POST.get('Username_TSA')
#     Date_Time=request.POST.get('Date_Time_TSA')

#     if Username == 'all':

#         for TSA in Consumer.objects.all().filter(Username__contains="tsa",Date_Time__contains=Date_Time).values_list('Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
#             'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
#             'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
#             'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
#             'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
#             'NoofDigits','SurveyorRemark'):
#             writer.writerow(TSA)
#     else:

#         for TSA in Consumer.objects.all().filter(Username=Username,Date_Time__contains=Date_Time).values_list('Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
#             'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
#             'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
#             'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
#             'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
#             'NoofDigits','SurveyorRemark'):
#             writer.writerow(TSA)

#     return response



# def index(request):
#     if request.method == 'POST':
#             form = ConsumerForm(request.POST) 

#             Username = request.POST['Username']
#             Date_Time = request.POST['Date_Time']

#             try:
#                 NKT = Consumer.objects.get(Username_NKT=Username,Date_Time_NKT=Date_Time)   

#                 request.session['Username'] = Username
#                 request.session['Date_Time'] = Date_Time

#             except Consumer.DoesNotExist:
#                 NKT= None
                         
#             if NKT is not None:
#                 return redirect('/consumer_NKT')                                           
#             else:
#                 return render(request, 'index.html')

#     return render(request,"index.html") 

# def consumer_NKT(request):
#     response = HttpResponse(
#         content_type='text/csv',
#         headers={'Content-Disposition': 'attachment; filename="consumer(NKT).csv"'},
#     )

#     writer = csv.writer(response)
#     writer.writerow(['Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
#             'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
#             'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
#             'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
#             'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
#             'NoofDigits','SurveyorRemark'])

#     Username=request.POST.get('Username_NKT')
#     Date_Time=request.POST.get('Date_Time_NKT')

#     if Username == 'all':

#         for NKT in Consumer.objects.all().filter(Username__contains="nkt",Date_Time__contains=Date_Time).values_list('Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
#             'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
#             'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
#             'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
#             'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
#             'NoofDigits','SurveyorRemark'):
#             writer.writerow(NKT)
#     else:

#         for NKT in Consumer.objects.all().filter(Username=Username,Date_Time__contains=Date_Time).values_list('Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
#             'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
#             'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
#             'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
#             'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
#             'NoofDigits','SurveyorRemark'):
#             writer.writerow(NKT)

#     return response







