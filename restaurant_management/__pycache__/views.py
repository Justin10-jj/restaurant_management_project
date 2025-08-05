class MenuAPI(APIView):
    def get(self,request):
        menu=[
            {
                "nmae":"margherita pizza",
                "description":"classsic pizza",
                "price":9.99
            }
        ]