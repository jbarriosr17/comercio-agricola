
import React, { useEffect, useState } from 'react'
import { getProducts, createOrder } from './api'

export default function App() {
  const [products, setProducts] = useState([])
  const [selected, setSelected] = useState({})
  const [customer, setCustomer] = useState('')
  const [msg, setMsg] = useState('')

  useEffect(() => {
    getProducts().then(setProducts).catch(e => setMsg(e.message))
  }, [])

  function toggle(p) {
    setSelected(s => {
      const next = {...s}
      next[p.id] = (next[p.id] || 0) + 1
      return next
    })
  }

  async function submit() {
    setMsg('')
    try {
      const items = Object.entries(selected).map(([product_id, quantity]) => ({
        product_id: Number(product_id), quantity
      }))
      const res = await createOrder({ customer_name: customer || 'Cliente', items })
      setSelected({})
      setMsg(`Pedido creado #${res.id}`)
    } catch (e) {
      setMsg(e.message)
    }
  }

  return (
    <div style={{fontFamily:'system-ui', maxWidth: 960, margin: '2rem auto', padding: '0 1rem'}}>
      <h1>Comercio Agrícola - UMG </h1>
      <p>Demostración de frontend: listar productos y crear pedidos.</p>

      {msg && <div style={{padding: '0.5rem', border: '1px solid', marginBottom: '1rem'}}>{msg}</div>}

      <label>Cliente:&nbsp;
        <input value={customer} onChange={e => setCustomer(e.target.value)} placeholder="Nombre" />
      </label>

      <h2>Productos</h2>
      <ul>
        {products.map(p => (
          <li key={p.id} style={{marginBottom: 8}}>
            <strong>{p.name}</strong> — {p.category} — Q{p.price} — stock: {p.stock}
            <button style={{marginLeft: 8}} onClick={() => toggle(p)}>Agregar</button>
          </li>
        ))}
      </ul>

      <h2>Carrito</h2>
      <pre>{JSON.stringify(selected, null, 2)}</pre>
      <button onClick={submit} disabled={Object.keys(selected).length===0}>Crear pedido</button>
    </div>
  )
}
