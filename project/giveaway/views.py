from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ConditionSerializer, AuthorSerializer, GenreSerializer, BookSerializer
from .models import Book, Author, Genre, Condition


# todo: test when i create book


# Book views
class BookListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        books = Book.objects.all()


        if books:
            serializer = BookSerializer(books, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={'No books in db'}, status=status.HTTP_204_NO_CONTENT)


class BookCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        book.delete()
        return Response(data={'deleted'}, status=status.HTTP_204_NO_CONTENT)


class BookEditAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)

        serializer = BookSerializer(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Author Views
class AuthorCreateAPIView(BookEditAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorListAPIView(BookEditAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        authors = Author.objects.all()

        if authors:
            serializer = AuthorSerializer(authors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'No authors in the database'}, status=status.HTTP_204_NO_CONTENT)


class AuthorDeleteAPIView(BookEditAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        author = Author.objects.filter(pk=pk)

        author.delete()
        return Response(data={None}, status=status.HTTP_204_NO_CONTENT)


class AuthorEditAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        author = get_object_or_404(Author, id=pk)

        serializer = AuthorSerializer(author, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



