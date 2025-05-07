import React from 'react';
import './i18n';
import { useTranslation } from 'react-i18next';

function App() {
  const { t, i18n } = useTranslation();

  return (
    <div>
      <select onChange={(e) => i18n.changeLanguage(e.target.value)}>
        <option value="en">English</option>
        <option value="hi">Hindi</option>
        <option value="mr">Marathi</option>
        <option value="ta">Tamil</option>
      </select>
      <h1>{t('Mark Attendance')}</h1>
    </div>
  );
}

export default App;
