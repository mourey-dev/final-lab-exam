import { createWebHistory, createRouter } from "vue-router";

import BookList from "./components/BookList.vue";
import BorrowTransactionList from "./components/BorrowTransactionList.vue";

const routes = [
  { path: "/", component: BookList },
  { path: "/borrow-transaction", component: BorrowTransactionList },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
