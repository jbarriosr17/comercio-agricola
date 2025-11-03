
export const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export async function getProducts() {
  const r = await fetch(`${API_BASE}/api/v1/products`)
  if (!r.ok) throw new Error('Error al cargar productos')
  return r.json()
}

export async function createOrder(payload) {
  const r = await fetch(`${API_BASE}/api/v1/orders`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  })
  if (!r.ok) {
    const err = await r.json().catch(() => ({}))
    throw new Error(err.detail || 'Error creando pedido')
  }
  return r.json()
}
