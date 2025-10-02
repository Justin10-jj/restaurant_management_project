class ContactFormSubmissionSerializer(serilazers.ModelSerializer):
    class Meta:
        model=ContactFormSubmission 
        fields=["id","email","message","created_at"]

        
        
class DailySpecialSerializer(serilazers.ModelSerializer):
    class Meta:
        model=MenuItem
        field=['id','name','description','price']


class TableSerializer(serilaizers.ModelSerializer):
    class Meta:
        model=Table 
        field=["table_number","capacity","is_availabile"]
        