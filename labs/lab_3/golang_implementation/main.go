package main

import (
	"image"
	"image/color"
	"image/jpeg"
	"log"
	"math"
	"os"
)

// Создание Гауссового ядра
func createGaussianKernel(size int, sigma float64) [][]float64 {
	kernel := make([][]float64, size)
	sum := 0.0
	radius := size / 2

	for y := -radius; y <= radius; y++ {
		row := make([]float64, size)
		for x := -radius; x <= radius; x++ {
			exponent := -(float64(x*x+y*y) / (2 * sigma * sigma))
			value := math.Exp(exponent) / (2 * math.Pi * sigma * sigma)
			row[x+radius] = value
			sum += value
		}
		kernel[y+radius] = row
	}

	// Нормализация ядра
	for y := 0; y < size; y++ {
		for x := 0; x < size; x++ {
			kernel[y][x] /= sum
		}
	}

	return kernel
}

// Применение свёртки
func applyConvolution(img image.Image, kernel [][]float64) *image.RGBA {
	bounds := img.Bounds()
	width, height := bounds.Max.X, bounds.Max.Y
	output := image.NewRGBA(bounds)
	radius := len(kernel) / 2

	for y := bounds.Min.Y; y < bounds.Max.Y; y++ {
		for x := bounds.Min.X; x < bounds.Max.X; x++ {
			var rSum, gSum, bSum float64

			for ky := -radius; ky <= radius; ky++ {
				for kx := -radius; kx <= radius; kx++ {
					ix := x + kx
					iy := y + ky

					if ix >= 0 && ix < width && iy >= 0 && iy < height {
						r, g, b, _ := img.At(ix, iy).RGBA()
						weight := kernel[ky+radius][kx+radius]

						rSum += float64(r>>8) * weight
						gSum += float64(g>>8) * weight
						bSum += float64(b>>8) * weight
					}
				}
			}

			// Ограничиваем значения (0-255)
			output.Set(x, y, color.RGBA{
				R: uint8(clamp(rSum, 0, 255)),
				G: uint8(clamp(gSum, 0, 255)),
				B: uint8(clamp(bSum, 0, 255)),
				A: 255,
			})
		}
	}

	return output
}

// Ограничение значения в диапазоне [min, max]
func clamp(value, min, max float64) float64 {
	if value < min {
		return min
	}
	if value > max {
		return max
	}
	return value
}

func main() {
	// Открываем изображение
	file, err := os.Open("files/1.jpg")
	if err != nil {
		log.Fatalf("Failed to open image: %v", err)
	}
	defer file.Close()

	img, _, err := image.Decode(file)
	if err != nil {
		log.Fatalf("Failed to decode image: %v", err)
	}

bounds := img.Bounds()
    grayImg := image.NewGray(bounds)

	for y := bounds.Min.Y; y < bounds.Max.Y; y++ {
		for x := bounds.Min.X; x < bounds.Max.X; x++ {
			c := img.At(x, y)

			grayColor := color.GrayModel.Convert(c).(color.Gray)
			grayImg.Set(x, y, grayColor)
		}
	}

	// Создание ядра Гаусса
	kernel := createGaussianKernel(5, 2.0)

	// Применение Гауссового размытия
	blurred := applyConvolution(grayImg, kernel)

	// Сохранение результата
	outputFile, err := os.Create("files/2.jpg")
	if err != nil {
		log.Fatalf("Failed to create output file: %v", err)
	}
	defer outputFile.Close()

	err = jpeg.Encode(outputFile, blurred, nil)
	if err != nil {
		log.Fatalf("Failed to save image: %v", err)
	}

	log.Println("Gaussian blur applied and saved to 2.jpg")
}
