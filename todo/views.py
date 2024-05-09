from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Todo
from .serializers import (
    TodosimpleSerializer,
    TodoDetailSerializer,
    TodoCreateSerializer
)

# generics 기반 뷰
class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodosimpleSerializer

    def perform_create(self, serializer):
        serializer.save()

class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer

class DoneTodoListAPIView(generics.ListAPIView):
    serializer_class = TodosimpleSerializer

    def get_queryset(self):
        return Todo.objects.filter(complete=True)

# APIView 기반 뷰
class TodosAPIView(APIView):
    def get(self, request):  # 전체 조회
        todos = Todo.objects.filter(complete=False)
        serializer = TodosimpleSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):  # 생성
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoAPIView(APIView):  # 상세 조회
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):  # 수정
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoneTodosAPIView(APIView):  # 완료
    def get(self, request):
        dones = Todo.objects.filter(complete=True)
        serializer = TodosimpleSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoneTodoAPIView(APIView):  # 완료 조회
    def get(self, request, pk):
        done = get_object_or_404(Todo, id=pk)
        done.complete = True
        done.save()
        serializer = TodoDetailSerializer(done)
        return Response(serializer.data, status=status.HTTP_200_OK)
