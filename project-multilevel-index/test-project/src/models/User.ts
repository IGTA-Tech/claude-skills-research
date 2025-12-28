/**
 * Input: None (type definitions only)
 * Output: User interface, CreateUserDTO interface
 * Pos: Data Layer - User domain model, defines user entity structure
 *
 * 🔄 Self-reference: When this file changes, update:
 * - This file header
 * - src/models/FOLDER_INDEX.md
 * - PROJECT_INDEX.md
 */

export interface User {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
}

export interface CreateUserDTO {
  name: string;
  email: string;
}
