// categoryStore.js
import { defineStore } from "pinia";
import { ref } from "vue";

export const useCategoryStore = defineStore('category', () => {
    const categories = ref([])

    const fetchCategories = async () => {
        try {
            const response = await fetch('http://localhost:5000/categories');
            if (!response.ok) {
                throw new Error(`HTTP Error! Status: ${response.status}`);
            }
            const data = await response.json()
            categories.value = data
        } catch (error) {
            console.log("ERROR", error.message)
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

            const newCategory = await response.json()
            if (!response.ok) {
                throw new Error(newCategory.message);
            }
            
            categories.value.push(newCategory)
            return newCategory
        } catch (error) {
            console.log(error)
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
        categories, 
        fetchCategories,
        addCategory
    }
})