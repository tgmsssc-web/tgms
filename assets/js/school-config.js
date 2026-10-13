
/**
 * Central Telangana Model Schools website system
 * Loads school data from a JSON configuration file.
 */

async function loadSchoolConfig(schoolId) {
  if (!/^[a-z0-9-]+$/.test(schoolId)) {
    throw new Error("Invalid school ID.");
  }

  const configUrl = `../../schools-data/${schoolId}.json`;

  const response = await fetch(configUrl);

  if (!response.ok) {
    throw new Error("School configuration could not be loaded.");
  }

  return await response.json();
}

function setSchoolText(selector, value) {
  const element = document.querySelector(selector);

  if (element && typeof value === "string" && value.trim()) {
    element.textContent = value;
  }
}
