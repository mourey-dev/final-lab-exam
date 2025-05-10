<template>
  <div class="p-6">
    <div class="flex items-center justify-between mb-4">
      <h1 class="text-xl font-bold">Book Transactions</h1>
      <div class="flex gap-4">
        <button
          class="border py-1 px-2 font-bold cursor-pointer rounded bg-blue-600 text-white hover:bg-blue-700"
          @click="isBorrowModalOpen = true"
        >
          Borrow Book
        </button>
        <button
          class="border py-1 px-2 font-bold cursor-pointer rounded bg-blue-600 text-white hover:bg-blue-700"
          @click="isReturnModalOpen = true"
        >
          Return Book
        </button>
      </div>
    </div>

    <div class="overflow-x-auto">
      <table
        class="min-w-full bg-white border border-gray-200 shadow rounded-lg border-collapse"
      >
        <thead>
          <tr class="bg-gray-100 text-gray-700 text-left">
            <th class="py-3 px-4 border text-center">Borrower Name</th>
            <th class="py-3 px-4 border text-center">Book Borrowed</th>
            <th class="py-3 px-4 border text-center">Date</th>
            <th class="py-3 px-4 border text-center">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="transaction in transactions"
            :key="transaction.id"
            class="hover:bg-gray-50 transition duration-150"
          >
            <td class="py-3 px-4 border text-center">
              {{ transaction.user.first_name }} {{ transaction.user.last_name }}
            </td>
            <td class="py-3 px-4 border text-center">
              {{ transaction.book.title }}
            </td>
            <td class="py-3 px-4 border text-center">
              {{ transaction.date }}
            </td>
            <td class="py-3 px-4 border text-center capitalize">
              {{ transaction.status }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Borrow Modal -->
    <BorrowFormModal
      :visible="isBorrowModalOpen"
      @close="isBorrowModalOpen = false"
      @saved="fetchTransactions"
    />

    <!-- Return Modal -->
    <ReturnFormModal
      :visible="isReturnModalOpen"
      :transactions="transactions"
      @close="isReturnModalOpen = false"
      @saved="fetchTransactions"
    />
  </div>
</template>

<script>
import axios from "axios";
import BorrowFormModal from "@/components/BorrowFormModal.vue";
import ReturnFormModal from "@/components/ReturnFormModal.vue";

export default {
  name: "BorrowTransactionList",
  components: {
    BorrowFormModal,
    ReturnFormModal,
  },
  data() {
    return {
      transactions: [],
      isBorrowModalOpen: false,
      isReturnModalOpen: false,
    };
  },
  mounted() {
    this.fetchTransactions();
  },
  methods: {
    async fetchTransactions() {
      try {
        const response = await axios.get(
          "http://localhost:8000/api/transactions/"
        );
        this.transactions = response.data.borrow_transactions;
      } catch (error) {
        console.error("Error fetching transactions:", error);
      }
    },
  },
};
</script>
