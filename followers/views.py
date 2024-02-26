from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import followers
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = followers.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class= FollowerSerializer
    queryset = followers.objects.all()
    
    