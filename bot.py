import discord
from discord.ext import commands

# すべてのインテントを有効にしてボット.を作成
インテント = discord.Intents.all()
ボット = commands.Bot(command_prefix=",", intents=インテント)

@ボット.event
async def on_ready():
    print("準備はできている！")

@ボット.event
async def on_message(メッセージ):
    if メッセージ.content.lower() == ",ロック":
        # メッセージからギルドを取得
        ギルド = メッセージ.guild

        if ギルド is None:
            return
        
        # ボットの最高ロールの位置を取得
        ボットメンバー = ギルド.get_member(ボット.user.id)
        ボット・ロール・ポジション = max(役職.position for 役職 in ボットメンバー.roles)

        for チャンネル in ギルド.channels:
            if isinstance(チャンネル, (discord.TextChannel, discord.VoiceChannel, discord.CategoryChannel)):
                for 役職 in ギルド.roles:
                    if 役職.position < ボット・ロール・ポジション and not 役職.managed:
                        try:
                            await チャンネル.set_permissions(役職, view_channel=False)
                            print(f"チャンネル{チャンネル.name}のロール{役職.name}のパーミッションが更新されました。")
                        except Exception as e:
                            print(f"チャンネル{チャンネル.name}のロール{役職.name}のパーミッションの更新に失敗しました： {e}")

ボット.run("隠されたトークン")
