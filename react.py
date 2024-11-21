react = """
/**
 * 示例组件，包含数据类型定义，block类型定义，组件实现，组件demo，类型扩展
 */

import { FC } from 'react';
import { BaseBlockType } from './types';
import { cn } from '@/lib/utils';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { injectBlock } from './render';

/* 注意，以下所有的 [ExampleBlock] 在实际使用中需要替换为 [XXXBlock] */

// required: 数据类型
// >>> 这里定义此组件需要的数据类型，不含组件type，只包含组件渲染必须的数据
export interface ExampleBlockData {
  title: string;
  description?: string;
  body: string;
  footer?: string;
}

// required: 类型名称
// >>> 这里定义组件类型名称
const ExampleBlockTypeName = 'example' as const;

// required: block类型
// >>> 这里根据data和type，使用 BaseBlockType 包装成 Block类型
export type ExampleBlock = BaseBlockType<typeof ExampleBlockTypeName, ExampleBlockData>;

// optional: demo数据
// >> 可选，示例数据，内容需要与上面的 ExampleBlock 类型定义一致
const Demo: ExampleBlock = {
  type: 'example',
  data: {
    title: 'example title',
    description: 'example description',
    body: 'example body content',
  },
};

interface ExampleBlockProps {
  className?: string;
  block: ExampleBlock; // >> 这里传入以上定义类型的数据
}
// required: 组件实现
// >>> 这里就是具体的组件实现了
const ExampleBlockComponent: FC<ExampleBlockProps> = (props) => {
  const { className, block } = props;
  return (
    <Card className={cn('w-full', className)}>
      <CardHeader>
        <CardTitle>{block.data.title}</CardTitle>
        {block.data.description ? (
          <CardDescription>{block.data.description}</CardDescription>
        ) : null}
      </CardHeader>
      <CardContent>
        <p>{block.data.body}</p>
      </CardContent>
      {block.data.footer ? (
        <CardFooter>
          <p>{block.data.footer}</p>
        </CardFooter>
      ) : null}
    </Card>
  );
};

export default ExampleBlockComponent;

// optional: 组件demo
// >> 可选：使用示例数据的组件
export const ExampleBlockDemo = () => {
  return <ExampleBlockComponent block={Demo} />;
};

// required: 扩展基础block类型
// >>> 重要！把当前的类型扩展到基础类型中，给外部使用
declare module '@/components/block/types' {
  interface AllBlockMap {
    [ExampleBlockTypeName]: ExampleBlock;
  }
}

// required: 将组件注入到渲染器
// >>> 重要！把组件注入到渲染器，以便可以在有对应block数据的时候可以选择此组件
export function inject() {
  injectBlock(ExampleBlockTypeName, ExampleBlockComponent);
}


"""