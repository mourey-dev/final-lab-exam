<template>
  <div
    v-if="visible"
    class="fixed inset-0 bg-black/60 flex items-center justify-center z-50"
  >
    <div class="bg-white rounded-lg w-full max-w-md p-6 shadow-lg">
      <h2 class="text-xl font-semibold mb-4">Return Book</h2>

      <form @submit.prevent="handleSubmit" class="grid gap-4">
        <div>
          <label class="block font-medium mb-1">Borrowed Transaction</label>
          <select
            v-model="selectedTransactionId"
            class="w-full border rounded px-3 py-2"
            required
          >
            <option disabled value="">Select a transaction</option>
            <option
              v-for="tx in borrowedTransactions"
              :key="tx.id"
              :value="tx.id"
            >
              {{ tx.user.first_name }} {{ tx.user.last_name }} - "{{
                tx.book.title
              }}"
            </option>
          </select>
        </div>

        <div>
          <label class="block font-medium mb-1">Return Date</label>
          <input
            type="date"
            v-model="returnDate"
            class="w-full border rounded px-3 py-2"
            required
          />
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
            class="px-4 py-2 rounded bg-green-600 text-white hover:bg-green-700"
          >
            Return
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";

const props = defineProps({
  visible: Boolean,
  transactions: Array, // All borrow transactions
});
const emit = defineEmits(["close", "saved"]);

const selectedTransactionId = ref("");
const returnDate = ref(new Date().toISOString().split("T")[0]);

const borrowedTransactions = computed(() =>
  props.transactions.filter((tx) => tx.status === "borrowed")
);

function resetForm() {
  selectedTransactionId.value = "";
  returnDate.value = new Date().toISOString().split("T")[0];
}

async function handleSubmit() {
  try {
    const transaction = props.transactions.find(
      (t) => t.id === selectedTransactionId.value
    );

    if (!transaction) throw new Error("Invalid transaction selected.");

    await axios.post(`http://localhost:8000/api/return/${transaction.id}/`, {
      date: returnDate.value,
    });

    emit("saved");
    close();
    toast.success("Success", {
      autoClose: 1500,
      pauseOnFocusLoss: false,
    });
  } catch (error) {
    console.error("Return failed:", error);
  }
}

function close() {
  resetForm();
  emit("close");
}
</script>
