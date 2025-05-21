<script setup lang="ts">
import { onMounted, ref } from 'vue'

type Data = {
  address: string
  port: number
}

const data = ref<Data | null>(null)

async function fetchData() {
  try {
    const response = await fetch('http://localhost:8000/list');
    if (!response.ok) throw new Error('Ошибка сети');
    data.value = await response.json();
  } catch (err) {
    console.log(err)
  }
}

onMounted(async () => {
  fetchData();
})
</script>

<template>
  <div>
    <div class="pidoras">
      {{ data?.address }}
    </div>
    <div class="kukumas">
      {{ data?.port }}
    </div>
  </div>

</template>

<style scoped>
.pidoras {
  color: black;
  width: 200px;
  background-color: aquamarine;
  text-decoration: underline;
}

.kukumas {
  width: 100px;
  background-color: blue;
  text-decoration: solid;
  border: 5px;
}
</style>
