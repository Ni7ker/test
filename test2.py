import React, { useState } from 'react';

function WishList() {
  const [wishes, setWishes] = useState([]);
  const [input, setInput] = useState('');

  // Inline-стили (выбраны для простоты и минимализма)
  const styles = {
    container: { maxWidth: '600px', margin: '20px auto', padding: '20px' },
    input: { padding: '8px', marginRight: '10px', width: '70%' },
    button: { padding: '8px 16px', backgroundColor: '#4CAF50', color: 'white', border: 'none' },
    list: { listStyle: 'none', padding: '0' },
    listItem: { display: 'flex', justifyContent: 'space-between', margin: '8px 0' }
  };

  const handleAdd = () => {
    if (input.trim()) {
      setWishes([...wishes, { id: Date.now(), text: input }]);
      setInput('');
    }
  };

  const handleDelete = (id) => {
    setWishes(wishes.filter(wish => wish.id !== id));
  };

  return (
    <div style={styles.container}>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        style={styles.input}
        placeholder="Добавить желание"
      />
      <button onClick={handleAdd} style={styles.button}>Добавить</button>
      
      {wishes.length === 0 ? (
        <p>Пока желаний нет</p>
      ) : (
        <ul style={styles.list}>
          {wishes.map(wish => (
            <li key={wish.id} style={styles.listItem}>
              {wish.text}
              <button onClick={() => handleDelete(wish.id)} style={{ ...styles.button, backgroundColor: '#f44336' }}>
                Удалить
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default WishList;

// Комментарии по стилям:
// 1. Inline-стили упрощают изоляцию стилей компонента.
// 2. Использованы базовые CSS-свойства для читаемости.
// 3. Цвета выбраны для контраста и доступности.

// Адаптация под бэкенд:
// 1. Добавить fetch-запросы к API (GET/POST/DELETE).
// 2. Реализовать обработку ошибок (try/catch).
// 3. Добавить индикатор загрузки (спиннер).
// 4. Кэшировать данные через React Query.
// 5. Настроить обновление данных в реальном времени (WebSocket).
