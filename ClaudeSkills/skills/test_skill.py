#!/usr/bin/env python3
"""
Seedream 4.0 Skill 测试脚本

这个脚本用于测试 Seedream 4.0 图像生成 skill 是否正确安装和配置。
"""

import os
import sys

def test_imports():
    """测试必要的库是否已安装"""
    print("🧪 测试 1: 检查依赖库...")
    try:
        import requests
        print("   ✅ requests 库已安装")
        return True
    except ImportError:
        print("   ❌ requests 库未安装")
        print("   请运行: pip install requests --break-system-packages")
        return False

def test_api_key():
    """测试 API 密钥是否已配置"""
    print("\n🧪 测试 2: 检查 API 密钥...")
    api_key = os.getenv('SEGMIND_API_KEY')
    if api_key:
        print(f"   ✅ API 密钥已设置: {api_key[:10]}...")
        return True
    else:
        print("   ⚠️  API 密钥未设置")
        print("   请运行: export SEGMIND_API_KEY='your_api_key'")
        return False

def test_script_exists():
    """测试生成脚本是否存在"""
    print("\n🧪 测试 3: 检查生成脚本...")
    script_path = "scripts/generate_image.py"
    if os.path.exists(script_path):
        print(f"   ✅ 脚本文件存在: {script_path}")
        return True
    else:
        print(f"   ❌ 脚本文件不存在: {script_path}")
        return False

def test_script_import():
    """测试是否可以导入生成器类"""
    print("\n🧪 测试 4: 检查脚本可导入性...")
    try:
        # 添加 scripts 目录到路径
        sys.path.insert(0, 'scripts')
        from generate_image import SeedreamImageGenerator
        print("   ✅ 成功导入 SeedreamImageGenerator")
        return True
    except Exception as e:
        print(f"   ❌ 导入失败: {e}")
        return False

def test_basic_generation():
    """测试基础图像生成(如果有 API 密钥)"""
    print("\n🧪 测试 5: 测试图像生成...")
    
    api_key = os.getenv('SEGMIND_API_KEY')
    if not api_key:
        print("   ⏭️  跳过(需要 API 密钥)")
        return None
    
    try:
        sys.path.insert(0, 'scripts')
        from generate_image import SeedreamImageGenerator
        
        print("   正在生成测试图像...")
        generator = SeedreamImageGenerator(api_key=api_key)
        
        paths = generator.generate(
            prompt="A simple test image: a red circle on white background, minimalist",
            size="2K",
            aspect_ratio="1:1",
            max_images=1,
            output_dir="./test_outputs"
        )
        
        print(f"   ✅ 成功生成图像: {paths[0]}")
        print(f"   📁 测试图像保存在: ./test_outputs/")
        return True
    except Exception as e:
        print(f"   ❌ 生成失败: {e}")
        return False

def main():
    """运行所有测试"""
    print("=" * 60)
    print("🚀 Seedream 4.0 Skill 测试套件")
    print("=" * 60)
    print()
    
    results = []
    
    # 运行测试
    results.append(("依赖检查", test_imports()))
    results.append(("API密钥配置", test_api_key()))
    results.append(("脚本文件", test_script_exists()))
    results.append(("脚本导入", test_script_import()))
    
    # 可选的生成测试
    gen_result = test_basic_generation()
    if gen_result is not None:
        results.append(("图像生成", gen_result))
    
    # 总结
    print("\n" + "=" * 60)
    print("📊 测试结果汇总")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result is True)
    failed = sum(1 for _, result in results if result is False)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"   {status} - {test_name}")
    
    print()
    print(f"总计: {passed}/{total} 通过")
    
    if failed == 0:
        print("\n🎉 所有测试通过!Skill 已正确配置。")
        return 0
    else:
        print(f"\n⚠️  有 {failed} 个测试失败,请检查配置。")
        return 1

if __name__ == "__main__":
    sys.exit(main())
