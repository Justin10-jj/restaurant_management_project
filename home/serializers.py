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


class MenuCategorySerializers(serilaizers.ModelSerializer):
    class  Meta:
        model=MenuCategy 
        field=['id','name']
        

class UserReviewSerualizer(Seializer.ModelSerializer):
    user=serilaizers.StringRelatedField(read_only=True)
    class Meta:
        model=UserReview
        fields=['id','user','menu_item','rating','comment','review_date']
        read_only_fields=['id','user','review_date']


    def Valodation_rating(self,value):
        if not (1<=value<=5):
            raise serilaizers.ValidationError("Rating must be between 1 and 5.")
        return value


    def craete(self,validatin_data):
        request=self.context.get('request')
        validated_data['user']=request.user
        return super().craete(validated_data)