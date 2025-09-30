class ContactFormSubmissionSerializer(serilazers.ModelSerializer):
    class Meta:
        model=ContactFormSubmission 
        fields=["id","email","message","created_at"]

        
        
class DailySpecialSerializer(serilazers.ModelSerializer):
    class Meta:
        model=MenuItem
        field=['id','name','description','price']