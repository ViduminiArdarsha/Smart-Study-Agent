// API Service for communicating with the backend
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api'

export const apiService = {
  // Study Sessions
  getStudySessions: async () => {
    const response = await fetch(`${API_BASE_URL}/sessions`)
    return response.json()
  },

  createStudySession: async (data: any) => {
    const response = await fetch(`${API_BASE_URL}/sessions`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
    return response.json()
  },

  updateStudySession: async (id: string, data: any) => {
    const response = await fetch(`${API_BASE_URL}/sessions/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
    return response.json()
  },

  deleteStudySession: async (id: string) => {
    const response = await fetch(`${API_BASE_URL}/sessions/${id}`, {
      method: 'DELETE',
    })
    return response.json()
  },

  // Syllabus
  getSyllabus: async () => {
    const response = await fetch(`${API_BASE_URL}/syllabus`)
    return response.json()
  },

  uploadSyllabus: async (file: File) => {
    const formData = new FormData()
    formData.append('file', file)
    const response = await fetch(`${API_BASE_URL}/syllabus`, {
      method: 'POST',
      body: formData,
    })
    return response.json()
  },

  // Feedback
  getFeedback: async () => {
    const response = await fetch(`${API_BASE_URL}/feedback`)
    return response.json()
  },

  submitFeedback: async (data: any) => {
    const response = await fetch(`${API_BASE_URL}/feedback`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
    return response.json()
  },
}
