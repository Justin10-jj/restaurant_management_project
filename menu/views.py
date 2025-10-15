Class MenuCategoryListView(generics.ListAPIView):
    queryset=MenuCategory.objects.all()
    serilizer_class=MenuCategorySerializer