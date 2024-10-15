# Meta Package
Name:           ros-humble-zstd-vendor
Version:        0.15.12
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://facebook.github.io/zstd/
Summary:        Meta package for ros2-humble-zstd_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-zstd_vendor
Requires:       ros2-humble-zstd_vendor-devel

Obsoletes: ros-humble-zstd-vendor < 0.15.12-1

%description
Zstd compression vendor package, providing a dependency for Zstd.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.12-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.11-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.9-1
- Update to latest release
