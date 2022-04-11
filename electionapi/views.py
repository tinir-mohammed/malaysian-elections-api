from urllib import response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import ElectionSerializer
from .models import ElectionResult
import pandas

class ElectionViewSet(APIView):
    # serializer_class = ElectionSerializer

    def post(self, request, *args, **kwargs):
        
        requestData = request.data
        seatID = requestData["seatID"]
        queryset = ElectionResult.objects.values_list().filter(seatID = seatID)
        queryset = list(queryset)
        queryResponse = {}
        queryResponseList = []

        for i in queryset:
            queryResponse = {}
            queryResponse["Seat ID"] = i[1]
            queryResponse["Candidate Name"] = i[2]
            queryResponse["Percent of total Votes"] = i[3]
            queryResponse["Status"] = i[4]
            queryResponseList.append(queryResponse)

        print(queryset)
        response = {
            "Result": queryResponseList
        }

        # Populate database
        # excel = "Election-Results.csv"
        # excel_data_df = pandas.read_csv(excel)

        # for index, row in excel_data_df.iterrows():
        #     print(row['Candidate Name'], row["Percent of total Votes"]) 
        #     new_result = ElectionResult.objects.create(
        #                                                 seatID= row["Seat ID"], 
        #                                                 candidName= row['Candidate Name'], 
        #                                                 percentWin= row["Percent of total Votes"],
        #                                                 status= row["Status"]
        #                                                 )
        #     new_result.save()

        return Response(response)