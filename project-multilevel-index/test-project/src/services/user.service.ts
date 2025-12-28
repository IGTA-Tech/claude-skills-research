/**
 * Input: User, CreateUserDTO from ../models/User; Logger from ../utils/logger
 * Output: UserService class (createUser/findById/findAll methods), EmailService class (sendWelcomeEmail method)
 * Pos: Service Layer - User domain service with email notification capability
 *
 * 🔄 Self-reference: When this file changes, update:
 * - This file header
 * - src/services/FOLDER_INDEX.md
 * - PROJECT_INDEX.md
 */

import { User, CreateUserDTO } from '../models/User';
import { Logger } from '../utils/logger';

// 新增依赖 - 这是一个结构性变更
class EmailService {
  static sendWelcomeEmail(email: string): void {
    console.log(`Sending welcome email to: ${email}`);
  }
}

export class UserService {
  private users: User[] = [];

  async createUser(dto: CreateUserDTO): Promise<User> {
    Logger.info(`Creating user: ${dto.name}`);

    const user: User = {
      id: Math.random().toString(36),
      name: dto.name,
      email: dto.email,
      createdAt: new Date()
    };

    this.users.push(user);

    // 发送欢迎邮件 - 使用新功能
    EmailService.sendWelcomeEmail(user.email);

    return user;
  }

  async findById(id: string): Promise<User | null> {
    return this.users.find(u => u.id === id) || null;
  }

  async findAll(): Promise<User[]> {
    return this.users;
  }
}
