# Meta Package
Name:           ros-humble-google-benchmark-vendor
Version:        0.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/google/benchmark
Summary:        Meta package for ros2-humble-google_benchmark_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-google_benchmark_vendor
Requires:       ros2-humble-google_benchmark_vendor-devel

Obsoletes: ros-humble-google-benchmark-vendor < 0.1.2-1

%description
This package provides Google Benchmark.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.2-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.2-1
- update to latest upstream
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- Initial humble build
