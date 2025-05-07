import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources: {
      en: { translation: { "Mark Attendance": "Mark Attendance" } },
      hi: { translation: { "Mark Attendance": "हाज़िरी दर्ज करें" } },
      mr: { translation: { "Mark Attendance": "हजेरी नोंदवा" } },
      ta: { translation: { "Mark Attendance": "வருகை பதிவு" } }
    },
    fallbackLng: 'en',
    interpolation: { escapeValue: false },
  });

export default i18n;
