<template>
    <div class="min-h-screen bg-gray-100 flex items-center justify-center">
      <div class="max-w-md w-full space-y-8">
        <div>
          <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">欢迎来到首页</h2>
        </div>
        <div class="flex justify-center">
          <router-link to="/register" class="mx-2 px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">注册</router-link>
          <router-link to="/login" class="mx-2 px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">登录</router-link>
        </div>
      </div>
    </div>
  </template>

  <script>
  export default {
    name: 'Home'
  }
  </script>
