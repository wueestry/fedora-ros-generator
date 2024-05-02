# Meta Package
Name:           ros-jazzy-google-benchmark-vendor
Version:        0.5.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/google/benchmark
Summary:        Meta package for ros2-jazzy-google_benchmark_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-google_benchmark_vendor
Requires:       ros2-jazzy-google_benchmark_vendor-devel

Obsoletes: ros-jazzy-google-benchmark-vendor < 0.5.0-1

%description
This package provides Google Benchmark.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.5.0-1
- Update to latest release
