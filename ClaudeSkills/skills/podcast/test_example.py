#!/usr/bin/env python3
"""
播客生成器快速测试示例
Quick test example for podcast generator
"""

import asyncio
import os
from pathlib import Path

# 注意: 需要先将podcast-generator技能中的scripts/generate_podcast.py复制到当前目录
# 或者确保该模块在Python路径中
try:
    from generate_podcast import PodcastGenerator
except ImportError:
    print("❌ 错误: 找不到generate_podcast模块")
    print("请确保已经安装播客生成器技能,或将generate_podcast.py复制到当前目录")
    exit(1)


async def test_basic_generation():
    """测试基础播客生成"""
    print("=" * 60)
    print("测试1: 基础播客生成")
    print("=" * 60)
    
    # 从环境变量获取凭证
    app_id = os.getenv("VOLCANO_APP_ID")
    access_key = os.getenv("VOLCANO_ACCESS_KEY")
    
    if not app_id or not access_key:
        print("⚠️  警告: 未设置环境变量")
        print("请设置以下环境变量:")
        print("  export VOLCANO_APP_ID='你的APP_ID'")
        print("  export VOLCANO_ACCESS_KEY='你的ACCESS_KEY'")
        print()
        print("或者直接在代码中修改app_id和access_key的值")
        return False
    
    generator = PodcastGenerator(
        app_id=app_id,
        access_key=access_key
    )
    
    # 测试简短内容
    test_text = "分析下当前的大模型发展,包括GPT-4、Claude等模型的特点和应用场景。"
    output_path = "test_podcast.mp3"
    
    print(f"📝 测试内容: {test_text}")
    print(f"💾 输出路径: {output_path}")
    print()
    
    try:
        result = await generator.generate_podcast(
            input_text=test_text,
            output_path=output_path,
            audio_format="mp3",
            sample_rate=24000,
            speech_rate=0
        )
        
        if result['success']:
            print(f"✅ 测试成功!")
            print(f"   文件: {result['output_path']}")
            print(f"   大小: {result['file_size']:.2f} MB")
            print(f"   轮次: {result['rounds']}")
            return True
        else:
            print(f"❌ 测试失败: {result.get('error')}")
            return False
            
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False


async def test_custom_parameters():
    """测试自定义参数"""
    print()
    print("=" * 60)
    print("测试2: 自定义参数(快速语速 + 开场音乐)")
    print("=" * 60)
    
    app_id = os.getenv("VOLCANO_APP_ID")
    access_key = os.getenv("VOLCANO_ACCESS_KEY")
    
    if not app_id or not access_key:
        print("⚠️  跳过测试: 未设置环境变量")
        return False
    
    generator = PodcastGenerator(
        app_id=app_id,
        access_key=access_key
    )
    
    test_text = "今天我们来快速总结一下最近AI领域的重要进展。"
    output_path = "test_podcast_fast.mp3"
    
    print(f"📝 测试内容: {test_text}")
    print(f"💾 输出路径: {output_path}")
    print(f"⚡ 语速: 1.5倍速")
    print(f"🎵 开场音乐: 启用")
    print()
    
    try:
        result = await generator.generate_podcast(
            input_text=test_text,
            output_path=output_path,
            audio_format="mp3",
            speech_rate=50,  # 1.5倍速
            use_head_music=True
        )
        
        if result['success']:
            print(f"✅ 测试成功!")
            print(f"   文件: {result['output_path']}")
            print(f"   大小: {result['file_size']:.2f} MB")
            return True
        else:
            print(f"❌ 测试失败: {result.get('error')}")
            return False
            
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False


async def test_different_formats():
    """测试不同音频格式"""
    print()
    print("=" * 60)
    print("测试3: 不同音频格式(OGG Opus)")
    print("=" * 60)
    
    app_id = os.getenv("VOLCANO_APP_ID")
    access_key = os.getenv("VOLCANO_ACCESS_KEY")
    
    if not app_id or not access_key:
        print("⚠️  跳过测试: 未设置环境变量")
        return False
    
    generator = PodcastGenerator(
        app_id=app_id,
        access_key=access_key
    )
    
    test_text = "测试OGG Opus格式的音频生成。"
    output_path = "test_podcast.ogg"
    
    print(f"📝 测试内容: {test_text}")
    print(f"💾 输出路径: {output_path}")
    print(f"🎵 音频格式: OGG Opus")
    print()
    
    try:
        result = await generator.generate_podcast(
            input_text=test_text,
            output_path=output_path,
            audio_format="ogg_opus"
        )
        
        if result['success']:
            print(f"✅ 测试成功!")
            print(f"   文件: {result['output_path']}")
            print(f"   大小: {result['file_size']:.2f} MB")
            return True
        else:
            print(f"❌ 测试失败: {result.get('error')}")
            return False
            
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False


async def main():
    """运行所有测试"""
    print()
    print("🚀 播客生成器技能测试套件")
    print("=" * 60)
    print()
    print("📋 测试前检查:")
    print("  1. 已安装websockets库: pip install websockets")
    print("  2. 已设置环境变量:")
    print("     - VOLCANO_APP_ID")
    print("     - VOLCANO_ACCESS_KEY")
    print("  3. 网络连接正常")
    print()
    
    # 检查websockets
    try:
        import websockets
        print("✅ websockets库已安装")
    except ImportError:
        print("❌ websockets库未安装")
        print("   请运行: pip install websockets")
        return
    
    # 检查环境变量
    if os.getenv("VOLCANO_APP_ID") and os.getenv("VOLCANO_ACCESS_KEY"):
        print("✅ 环境变量已设置")
    else:
        print("⚠️  环境变量未设置 - 将跳过实际API调用测试")
    
    print()
    input("按Enter键开始测试...")
    print()
    
    # 运行测试
    results = []
    
    # 测试1: 基础生成
    results.append(await test_basic_generation())
    
    # 测试2: 自定义参数
    results.append(await test_custom_parameters())
    
    # 测试3: 不同格式
    results.append(await test_different_formats())
    
    # 输出总结
    print()
    print("=" * 60)
    print("测试总结")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"通过: {passed}/{total}")
    print(f"失败: {total - passed}/{total}")
    
    if passed == total:
        print()
        print("🎉 所有测试通过!")
        print()
        print("生成的文件:")
        for file in ["test_podcast.mp3", "test_podcast_fast.mp3", "test_podcast.ogg"]:
            if Path(file).exists():
                size = Path(file).stat().st_size / (1024 * 1024)
                print(f"  - {file} ({size:.2f} MB)")
    else:
        print()
        print("⚠️  部分测试失败,请检查错误信息")


if __name__ == "__main__":
    asyncio.run(main())
