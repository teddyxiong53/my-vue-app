<template>
  <div id="app">
    <nav class="bg-gray-800 p-4">
      <div class="container mx-auto flex justify-between items-center">
        <div>
          <router-link to="/" class="text-white px-3 py-2 rounded-md text-sm font-medium">首页</router-link>
          <router-link to="/register" class="text-white px-3 py-2 rounded-md text-sm font-medium">注册</router-link>
          <router-link to="/login" class="text-white px-3 py-2 rounded-md text-sm font-medium">登录</router-link>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
