<template>
  <header class="flex items-center justify-between p-6 bg-blue-700">
    <h1 class="text-white font-bold text-2xl">Library Management System</h1>
    <nav class="flex gap-4">
      <RouterLink
        :class="
          route.path === '/'
            ? 'text-blue-300 font-medium underline'
            : 'hover:text-blue-300'
        "
        to="/"
      >
        Book
      </RouterLink>
      <RouterLink
        :class="
          route.path === '/borrow-transaction'
            ? 'text-blue-300 font-medium underline'
            : 'hover:text-blue-300 text-white'
        "
        to="/borrow-transaction"
      >
        Borrow
      </RouterLink>
    </nav>
  </header>
  <main>
    <RouterView />
  </main>
</template>

<script setup>
import { useRoute } from "vue-router";

const route = useRoute();
</script>
