# Meta Package
Name:           ros-iron-zstd-vendor
Version:        0.22.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://facebook.github.io/zstd/
Summary:        Meta package for ros2-iron-zstd_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-zstd_vendor
Requires:       ros2-iron-zstd_vendor-devel

Obsoletes: ros-iron-zstd-vendor < 0.22.6-1

%description
Zstd compression vendor package, providing a dependency for Zstd.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.22.6-1
- Update to latest upstream
