from moviepy.editor import VideoFileClip, clips_array

def merge_gifs(gif_paths, output_path, direction='horizontal'):
    # 读取GIF文件
    clips = [VideoFileClip(gif_path) for gif_path in gif_paths]
    
    if direction == 'horizontal':
        # 水平拼接: [[clip1, clip2]]表示一行两列
        arrangement = [clips]
    else:
        # 垂直拼接: [[clip1], [clip2]]表示两行一列
        arrangement = [[clip] for clip in clips]
    
    # 创建视频矩阵
    final_clip = clips_array(arrangement)
    
    # 导出为GIF
    final_clip.write_gif(output_path)
    
    # 关闭所有clips
    for clip in clips:
        clip.close()
    final_clip.close()


# 使用示例：
# clips = 'gif/foldchair_102255.gif gif/laptop_10211.gif gif/blade_103706.gif gif/scissor_11100.gif gif/stapler_103111.gif gif/storage_45135.gif'.split(' ')
# merge_gifs(clips[:2], 'synthetic_2p_1.gif', 'horizontal')
# merge_gifs(clips[2:4], 'synthetic_2p_2.gif', 'horizontal')
# merge_gifs(clips[4:6], 'synthetic_2p_3.gif', 'horizontal')
# clips = 'synthetic_2p_1.gif synthetic_2p_2.gif synthetic_2p_3.gif'.split(' ')
# merge_gifs(clips, 'synthetic_2p.gif', 'vertical')

# clips = 'gif/cabinet_1r2p_transparent.gif gif/cabinet_3r_white.gif gif/cabinet_1r_white.gif gif/washingmachine_1r.gif gif/real_fridge.gif gif/real_storage.gif'.split(' ')
# merge_gifs(clips[:2], 'real_1.gif', 'horizontal')
# merge_gifs(clips[2:4], 'real_2.gif', 'horizontal')
# merge_gifs(clips[4:6], 'real_3.gif', 'horizontal')
# clips = 'real_1.gif real_2.gif real_3.gif'.split(' ')
# merge_gifs(clips, 'real.gif', 'vertical')

# clips = 'gif/fridge_10489.gif gif/oven_101908.gif gif/storage_45503.gif gif/storage_47648.gif gif/table_25493.gif gif/table_31249.gif'.split(' ')
# merge_gifs(clips[:2], 'synthetic_mp_1.gif', 'horizontal')
# merge_gifs(clips[2:4], 'synthetic_mp_2.gif', 'horizontal')
# merge_gifs(clips[4:6], 'synthetic_mp_3.gif', 'horizontal')
# clips = 'synthetic_mp_1.gif synthetic_mp_2.gif synthetic_mp_3.gif'.split(' ')
# merge_gifs(clips, 'synthetic_mp.gif', 'vertical')

clips = 'gif/real_fridge.gif gif/real_fridge_paris.gif gif/real_storage.gif gif/real_storage_paris.gif'.split(' ')
merge_gifs(clips[:2], 'comparison_1.gif', 'vertical')
merge_gifs(clips[2:4], 'comparison_2.gif', 'vertical')
clips = 'comparison_1.gif comparison_2.gif'.split(' ')
merge_gifs(clips, 'comparison.gif', 'horizontal')