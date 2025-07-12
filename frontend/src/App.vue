<template>
  <div>
    <h1>Valor del Dólar</h1>
    <button @click="login" v-if="!token">Login</button>
    <div ref="plot" style="width: 100%; height: 500px;"></div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'
import Plotly from 'plotly.js-dist-min'

const token = ref(null)
const plot = ref(null)

const login = async () => {
  const res = await axios.post('http://localhost:8000/login',
    new URLSearchParams({ username: 'demo', password: 'demo' }),
    { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
  )
  token.value = res.data.access_token
  await fetchData()
}

const fetchData = async () => {
  const res = await axios.get('http://localhost:8000/data/parquet', {
    headers: { Authorization: `Bearer ${token.value}` }
  })

  const data = [{
    x: res.data.map(d => d.timestamp),
    y: res.data.map(d => d.valor_dolar),
    type: 'scatter',
    mode: 'lines+markers',
    marker: { color: '#2f9d98' }
  }]

  const layout = {
    title: 'Valor del Dólar en el Tiempo',
    xaxis: { title: 'Fecha', type: 'date' },
    yaxis: { title: 'CLP' },
    plot_bgcolor: '#f8f9fa',
    paper_bgcolor: '#fff'
  }

  Plotly.newPlot(plot.value, data, layout, {responsive: true})
}
</script>
