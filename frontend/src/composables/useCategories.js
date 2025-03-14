import { ref } from 'vue';

const categories = ref([]);


const fetchCategories = async () => {
  try {
    const response = await fetch('http://localhost:5000/api/categories');

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.message);
    }
    categories.value = data;
  } catch (error) {
    console.error("ERROR", error.message);
  }
};

const addCategory = async (categoryName) => {
  try {
      const response = await fetch('http://localhost:5000/api/categories', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': localStorage.getItem('token')
          },
          body: JSON.stringify({ name: categoryName })
      });

      const data = await response.json()
      if (!response.ok) {
          throw new Error(data.message);
      }
      categories.value.push(data)
  } catch (error) {
      console.log("ERROR", error.message)
      throw error
  }
}

const updateCategory = async (categoryId, categoryName) => {
  try {
      const response = await fetch(`http://localhost:5000/api/categories`, {
          method: 'PUT',
          headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': localStorage.getItem('token')
          },
          body: JSON.stringify({ existingCategoryId: categoryId, newCategoryName: categoryName })
      });

      const data = await response.json();
      if (!response.ok) {
          throw new Error(data.message);
      }

      const index = categories.value.findIndex(cat => cat.id === categoryId);
      if (index !== -1) {
          categories.value[index] = data;
      }
  } catch (error) {
      console.log("ERROR", error.message);
      throw error

  }
};


const deleteCategory = async (categoryId) => {
  try {
    const response = await fetch(`http://localhost:5000/api/categories`, {
      method: 'DELETE',
      headers: {
          'Content-Type': 'application/json',
          'Authentication-Token': localStorage.getItem('token')
      },
      body: JSON.stringify({ id: categoryId })
    })
    
    const data = await response.json();
      if (!response.ok) {
          throw new Error(data.message);
      }
    
    categories.value = categories.value.filter(cat => cat.id !== parseInt(categoryId))
  } catch (error) {
    console.log("ERROR", error.message)
    throw error
  }
}


export function useCategories() {
  return {
    categories,
    fetchCategories,
    addCategory,
    updateCategory,
    deleteCategory
  };
}
