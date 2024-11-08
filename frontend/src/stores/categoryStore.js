// categoryStore.js
import { defineStore } from "pinia";
import { ref } from "vue";

export const useCategoryStore = defineStore('category', () => {
    const allCategories = ref([])
    const loading = ref(false)

    const fetchAllCategories = async () => {
        try {
            loading.value = true
            const response = await fetch('http://localhost:5000/categories');
            if (!response.ok) {
                throw new Error(`HTTP Error! Status: ${response.status}`);
            }
            const jsonData = await response.json()
            allCategories.value = jsonData
        } catch (error) {
            console.log("ERROR", error.message)
            error.value = error.message
        } finally {
            loading.value = false
        }
    }

    const addCategory = async (categoryName) => {
        try {
            const response = await fetch('http://localhost:5000/categories', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name: categoryName })
            });
            if (!response.ok) {
                throw new Error(`HTTP Error! Status: ${response.status}`);
            }
            const newCategory = await response.json()
            // Add to existing categories - no need to refetch
            allCategories.value.push(newCategory)
            return newCategory
        } catch (error) {
            console.log("ERROR", error.message)
            error.value = error.message
            throw error
        }
    }

    // const deleteCategory = async (categoryId) => {
    //     try {
    //         const response = await fetch(`http://localhost:5000/categories/${categoryId}`, {
    //             method: 'DELETE'
    //         });
    //         if (!response.ok) {
    //             throw new Error(`HTTP Error! Status: ${response.status}`);
    //         }
    //         // Remove from existing categories - no need to refetch
    //         allCategories.value = allCategories.value.filter(cat => cat.id !== categoryId)
    //     } catch (error) {
    //         console.log("ERROR", error.message)
    //         error.value = error.message
    //         throw error
    //     }
    // }

    return { 
        allCategories, 
        loading,
        fetchAllCategories,
        addCategory
    }
})