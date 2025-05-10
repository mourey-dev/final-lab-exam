<template>
  <div
    v-if="visible"
    class="fixed inset-0 bg-black/60 flex items-center justify-center z-50"
  >
    <div class="bg-white rounded-lg w-full max-w-lg p-6 shadow-lg">
      <h2 class="text-xl font-semibold mb-4">Borrow Book</h2>

      <form @submit.prevent="handleSubmit" class="grid grid-cols-2 gap-4">
        <div class="col-span-2">
          <label class="block font-medium mb-1">User</label>
          <select
            v-model="form.user"
            class="w-full border rounded px-3 py-2"
            required
          >
            <option disabled value="">Select a user</option>
            <option v-for="user in users" :key="user.id" :value="user.id">
              {{ user.first_name }} {{ user.last_name }}
            </option>
          </select>
        </div>

        <div class="col-span-2">
          <label class="block font-medium mb-1">Book</label>
          <select
            v-model="form.book"
            class="w-full border rounded px-3 py-2"
            required
          >
            <option disabled value="">Select a book</option>
            <option v-for="book in books" :key="book.id" :value="book.id">
              {{ book.title }}
            </option>
          </select>
        </div>

        <div>
          <label class="block font-medium mb-1">Date</label>
          <input
            type="date"
            v-model="form.date"
            class="w-full border rounded px-3 py-2"
            required
          />
        </div>

        <div class="col-span-2 flex justify-end gap-2 mt-4">
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
            Submit
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch, ref } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";

const props = defineProps({
  visible: Boolean,
});

const emit = defineEmits(["close", "saved"]);

const form = reactive({
  book: "",
  user: "",
  status: "borrowed", // Fixed status to 'borrowed'
  date: new Date().toISOString().split("T")[0], // Current date
});

const books = ref([]);
const users = ref([]);

watch(
  () => props.visible,
  async (newVal) => {
    if (newVal) {
      await fetchBooksAndUsers();
    }
  },
  { immediate: true }
);

async function fetchBooksAndUsers() {
  try {
    const booksResponse = await axios.get("http://localhost:8000/api/books/");
    const usersResponse = await axios.get("http://localhost:8000/api/users/");

    // Set books and users locally
    books.value = booksResponse.data;
    users.value = usersResponse.data;
  } catch (error) {
    console.error("Failed to fetch books or users:", error);
  }
}

function resetForm() {
  form.book = "";
  form.user = "";
  form.date = new Date().toISOString().split("T")[0];
}

async function handleSubmit() {
  try {
    await axios.post("http://localhost:8000/api/borrow/", form); // Endpoint for borrowing
    emit("saved"); // Notify parent that the book has been borrowed
    close(); // Close modal
    toast.success("Success", {
      autoClose: 1500,
      pauseOnFocusLoss: false,
    });
  } catch (error) {
    const errorResponse = error.response?.data;
    toast.error(errorResponse?.error || "Something went wrong.", {
      autoClose: 1500,
      pauseOnFocusLoss: false,
    });
  }
}

function close() {
  resetForm(); // Reset the form data
  emit("close"); // Close modal
}
</script>
