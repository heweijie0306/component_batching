Prompts = [
"""
//text-paragraph-gaussian
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { EyeIcon } from 'lucide-react'

export default function GaussianBlurCard() {
  return (
    <div className="p-8 bg-background flex items-center justify-center">
      <Card className="w-full max-w-md overflow-hidden relative">
        <div className="absolute inset-0 bg-gradient-to-r from-primary/30 to-secondary/30 blur-2xl" />
        <div className="absolute inset-0 backdrop-blur-sm bg-background/30" />
        <CardHeader className="relative">
          <CardTitle className="flex items-center gap-2 text-primary">
            <EyeIcon className="w-6 h-6" />
            <span>Gaussian Blur</span>
          </CardTitle>
        </CardHeader>
        <CardContent className="relative">
          <p className="text-foreground mb-4 first-letter:float-left first-letter:text-6xl first-letter:pr-2 first-letter:font-serif first-letter:text-primary first-letter:mt-1">
            Gaussian blur softens and blends images, creating a dreamy, out-of-focus effect. 
            It's often used to create depth and direct attention in designs.
          </p>
          <div className="flex justify-center">
            <Button variant="outline" className="bg-background/50 hover:bg-background/70 backdrop-blur-md">
              Explore Effect
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
""",




]