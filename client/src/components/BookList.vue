<template>
  <div class="p-6">
    <div class="flex items-center justify-between mb-4">
      <h1 class="text-xl font-bold">Book List</h1>
      <button
        class="border py-1 px-2 font-bold cursor-pointer rounded bg-blue-600 text-white hover:bg-blue-700"
        @click="openAddModal"
      >
        Add Book
      </button>
    </div>

    <div class="overflow-x-auto">
      <table
        class="min-w-full bg-white border border-gray-200 shadow rounded-lg border-collapse"
      >
        <thead>
          <tr class="bg-gray-100 text-gray-700 text-left">
            <th class="py-3 px-4 border text-center">Title</th>
            <th class="py-3 px-4 border text-center">Author</th>
            <th class="py-3 px-4 border text-center">ISBN</th>
            <th class="py-3 px-4 border text-center">Available Copies</th>
            <th class="py-3 px-4 border text-center">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="book in books"
            :key="book.id"
            class="hover:bg-gray-50 transition duration-150"
          >
            <td class="py-3 px-4 border text-center">{{ book.title }}</td>
            <td class="py-3 px-4 border text-center">{{ book.author }}</td>
            <td class="py-3 px-4 border text-center">{{ book.isbn }}</td>
            <td class="py-3 px-4 border text-center">
              {{ book.available_copies }}
            </td>
            <td class="py-3 px-4 border text-center">
              <button
                class="bg-yellow-500 text-white px-2 py-1 rounded mr-2 hover:bg-yellow-600"
                @click="openEditModal(book)"
              >
                Edit
              </button>
              <button
                class="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600"
                @click="openDeleteModal(book)"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal -->
    <BookFormModal
      :visible="isModalOpen"
      :book="selectedBook"
      @close="isModalOpen = false"
      @saved="handleSaved"
    />
  </div>
  <ConfirmDeleteModal
    :visible="isConfirmVisible"
    :itemName="bookToDelete?.title"
    @close="isConfirmVisible = false"
    @confirm="deleteBook"
  />
</template>
<script>
import ConfirmDeleteModal from "@/components/ConfirmDeleteModal.vue";
import axios from "axios";
import BookFormModal from "@/components/BookFormModal.vue";
import { toast } from "vue3-toastify";

export default {
  name: "BookList",
  components: {
    BookFormModal,
    ConfirmDeleteModal,
  },
  data() {
    return {
      books: [],
      isModalOpen: false,
      selectedBook: null,
      isConfirmVisible: false,
      bookToDelete: null,
    };
  },
  mounted() {
    this.fetchBooks();
  },
  methods: {
    openDeleteModal(book) {
      this.bookToDelete = book;
      this.isConfirmVisible = true;
    },
    async fetchBooks() {
      try {
        const response = await axios.get("http://localhost:8000/api/books/");
        this.books = response.data;
      } catch (error) {
        console.error("Error fetching books:", error);
      }
    },
    openAddModal() {
      this.selectedBook = null;
      this.isModalOpen = true;
    },
    openEditModal(book) {
      this.selectedBook = book;
      this.isModalOpen = true;
    },
    async deleteBook() {
      try {
        await axios.delete(
          `http://localhost:8000/api/books/${this.bookToDelete.id}/`
        );
        toast.success("Book deleted successfully", { autoClose: 1000 });
        this.isConfirmVisible = false;
        this.bookToDelete = null;
        this.fetchBooks(); // Refresh list
      } catch (error) {
        const errorData = error.response?.data;
        toast.error(
          errorData?.error ? errorData.error : "Failed to delete book",
          { autoClose: 2000 }
        );
      }
    },
    handleSaved() {
      this.fetchBooks();
      this.isModalOpen = false;
    },
  },
};
</script>
