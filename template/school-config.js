
/**
 * Telangana Model Schools
 * Shared school configuration helper
 */

async function loadSchoolConfig(schoolId) {
  const response = await fetch(
    `../schools-data/${schoolId}.json`
  );

  if (!response.ok) {
    throw new Error("Unable to load school configuration.");
  }

  return response.json();
}

function setSchoolText(selector, value) {
  const element = document.querySelector(selector);

  if (element && value) {
    element.textContent = value;
  }
}
