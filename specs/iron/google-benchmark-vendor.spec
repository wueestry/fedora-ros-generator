# Meta Package
Name:           ros-iron-google-benchmark-vendor
Version:        0.3.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/google/benchmark
Summary:        Meta package for ros2-iron-google_benchmark_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-google_benchmark_vendor
Requires:       ros2-iron-google_benchmark_vendor-devel

Obsoletes: ros-iron-google-benchmark-vendor < 0.3.0-1

%description
This package provides Google Benchmark.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.3.0-1
- Update to latest release
