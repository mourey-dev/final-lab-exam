<template>
  <div
    v-if="visible"
    class="fixed inset-0 bg-black/60 flex items-center justify-center z-50"
  >
    <div class="bg-white rounded-lg w-full max-w-xl p-6 shadow-lg">
      <h2 class="text-xl font-semibold mb-4">
        {{ isEditMode ? "Update Book" : "Add New Book" }}
      </h2>

      <form @submit.prevent="handleSubmit" class="grid grid-cols-1 gap-4">
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block font-medium mb-1">ISBN</label>
            <input
              type="number"
              v-model="form.isbn"
              class="w-full border rounded px-3 py-2"
              required
            />
          </div>
          <div>
            <label class="block font-medium mb-1">Title</label>
            <input
              type="text"
              v-model="form.title"
              class="w-full border rounded px-3 py-2"
              required
            />
          </div>
          <div>
            <label class="block font-medium mb-1">Author</label>
            <input
              type="text"
              v-model="form.author"
              class="w-full border rounded px-3 py-2"
              required
            />
          </div>
          <div>
            <label class="block font-medium mb-1">Available Copies</label>
            <input
              type="number"
              v-model.number="form.available_copies"
              class="w-full border rounded px-3 py-2"
              required
            />
          </div>
        </div>

        <div class="flex justify-end gap-2 mt-4">
          <button
            type="button"
            @click="close"
            class="px-4 py-2 rounded border text-gray-600 hover:bg-gray-100"
          >
            Cancel
          </button>
          <button
            type="submit"
            class="px-4 py-2 rounded bg-blue-600 text-white hover:bg-blue-700"
          >
            {{ isEditMode ? "Update" : "Add" }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "vue3-toastify";

export default {
  name: "BookFormModal",
  props: {
    visible: Boolean,
    book: Object, // Book object to edit (null if adding)
  },
  data() {
    return {
      form: {
        isbn: "",
        title: "",
        author: "",
        available_copies: 0,
      },
    };
  },
  computed: {
    isEditMode() {
      return !!this.book;
    },
  },
  watch: {
    book: {
      immediate: true,
      handler(newVal) {
        if (newVal) {
          this.form = { ...newVal };
        } else {
          this.resetForm();
        }
      },
    },
  },
  methods: {
    async handleSubmit() {
      try {
        if (this.isEditMode) {
          await axios.put(
            `http://localhost:8000/api/books/${this.book.id}/`,
            this.form
          );
        } else {
          await axios.post("http://localhost:8000/api/books/", this.form);
        }
        this.$emit("saved"); // Notify parent to refresh the list
        this.close();
        toast.success("Success", {
          autoClose: 1500,
          pauseOnFocusLoss: false,
        });
      } catch (error) {
        const errorData = error.response?.data;
        toast.error(errorData.isbn[0] || "Something went wrong.", {
          autoClose: 2000,
          pauseOnFocusLoss: false,
        });
      }
    },
    resetForm() {
      this.form = {
        isbn: "",
        title: "",
        author: "",
        available_copies: 0,
      };
    },
    close() {
      this.$emit("close");
      this.resetForm();
    },
  },
};
</script>
